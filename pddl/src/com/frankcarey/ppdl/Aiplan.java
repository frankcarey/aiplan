package com.frankcarey.ppdl;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.util.Set;
import java.util.Stack;

import pddl4j.Domain;
import pddl4j.ErrorManager;
import pddl4j.PDDLObject;
import pddl4j.Parser;
import pddl4j.Problem;
import pddl4j.RequireKey;
import pddl4j.Source;
import pddl4j.ErrorManager.Message;
import pddl4j.InvalidExpException;
import pddl4j.exp.AndExp;
import pddl4j.exp.AtomicFormula;
import pddl4j.exp.Exp;
import pddl4j.exp.ExpID;
import pddl4j.exp.InitEl;
import pddl4j.exp.Literal;
import pddl4j.exp.NotAtomicFormula;
import pddl4j.exp.NotExp;
import pddl4j.exp.term.Substitution;
import pddl4j.exp.term.Variable;
import pddl4j.exp.term.Term;
import pddl4j.exp.action.Action;
import pddl4j.exp.action.ActionDef;
import pddl4j.exp.action.ActionID;
import pddl4j.exp.fcomp.FCompExp;
import pddl4j.exp.term.Constant;




public class Aiplan {

	public static void main(String[] args) {
	     // Checks the command line
	     if (args.length != 2) {
	         System.err.println("Invalid command line");
	     } else {
	         Properties options = null;
			// Creates an instance of the java pddl parser
	         Parser parser = new Parser(options);
	         try {
	        	Domain domain = parser.parse(new File(args[0]));
	         	Problem problem = parser.parse(new File(args[1]));
	     
		         PDDLObject obj = parser.link(domain, problem);
		         // Gets the error manager of the pddl parser
		         ErrorManager mgr = parser.getErrorManager();
		         // If the parser produces errors we print it and stop
		         if (mgr.contains(Message.ERROR)) {
		             mgr.print(Message.ALL);
		         } // else we print the warnings
		         else {
		             mgr.print(Message.WARNING);
		             System.out.println("\nParsing domain \"" + domain.getDomainName()
		                         + "\" done successfully ...");
		             System.out.println("Parsing problem \"" + problem.getProblemName()
		                         + "\" done successfully ...\n");
		         }
	         }
	         catch(FileNotFoundException e) {
	        	 
	         }
	     }

	}
}

