#!/usr/bin/env python3
## Windmill Cookie Review - Output formatted for Penetration Test Reports
## Douglas@RedSiege.com - @RackunSec
## Copy cookies in Burp Browser into a file
## Run this app and use -f <file>
from sys import argv as args ## App arguments
from sys import exit as exit ## Exit
from os import path as path ## Reading in the cookies file
from prettytable import PrettyTable ## Totally Tabular Output, Dude!
from sty import fg ## Printing Colors

## CookieReview Class
class Windmill:
    def __init__(self, cookieFile, domain):
        self.file = cookieFile
        self.domain = domain
        ## Red color for risk:
        self.RST='\033[0m' 
        self.RED=fg(197)
        self.sameSite = []
        self.secure = []
        self.httpOnly = []

## Review Cookies
    def cookieReview(self):
        print("[i] Reviewing session cookies for {}{}{}".format(self.RED,self.domain,self.RST))
        if path.exists(self.file):
            ## Make a Pretty Table:
            self.cookieTable = PrettyTable(["Cookie","Domain","HttpOnly","Secure","SameSite"])
            self.cookieTable.align["Cookie"] = "l" ## left align
            with open(self.file) as cFile:
                cLines = cFile.readlines() ## slurp into array
                for line in cLines: ## for each line in file
                    splitLine = line.split("\t") ## Split line into array
                    if self.domain in splitLine[2]: ## Only document the cookies from the domain
                        try:
                            ## translate for a report. Red X or None means trouble.
                            if splitLine[6] == "": ## HttpOnly
                                splitLine[6] = "{}✕{}".format(self.RED,self.RST) 
                                self.httpOnly.append(splitLine[0]) ## keep for later
                            if splitLine[7] == "": ## Secure
                                splitLine[7] = "{}✕{}".format(self.RED,self.RST)
                                self.secure.append(splitLine[0]) ## keep for later
                            if splitLine[8] == "None": ## SameSite
                                splitLine[8] = "{}None{}".format(self.RED,self.RST)
                                self.sameSite.append(splitLine[0]) ## keep for later
                            ## Make a PrettyTable row:
                            self.cookieTable.add_row([splitLine[0],splitLine[2],splitLine[6],splitLine[7],splitLine[8]])
                        except:
                            pass ## something wrong with input.
            print(self.cookieTable)
            if len(self.httpOnly) > 0:
                print("\n[i] The following cookies were missing the \"HttpOnly\" directive:\n")
                self.httpOnly.sort()
                for cookie in self.httpOnly:
                    print(" {}".format(cookie))

            if len(self.secure) > 0:
                print("\n[i] The following cookies were missing the \"Secure\" directive:\n")
                self.secure.sort()
                for cookie in self.secure:
                    print(" {}".format(cookie))

            if len(self.sameSite) > 0:
                print("\n[i] The following cookies have an insecure \"SameSite\" value:\n")
                self.secure.sort()
                for cookie in self.sameSite:
                    print(" {}".format(cookie))

        else:
            usage("Could not open {} for reading.".format(self.file))

def usage(errMsg):
    print("[!] ERROR: {}".format(errMsg))
    print("\n Usage: \n   python3 windmill.py -f <FILE> -d <DOMAIN>")
    exit()

def checkArgs(args):
    ## Check arguments
    if "-f" not in args:
        usage("Please provide a file name")
    if "-d" not in args:
        usage("Please provide a target domain")
    try:
        return Windmill(cookieFile=args[args.index("-f")+1],domain=args[args.index("-d")+1])
    except Exception as e:
        print(e) ## DEBUG
        usage("[!] Please review your arguments and ensure they are correct.")

if __name__ == "__main__":
    cookieObj = checkArgs(args)
    ## Flow through OK
    cookieObj.cookieReview()

