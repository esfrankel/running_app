//
//  ViewController.swift
//  aiRun
//
//  Created by Michael Sun on 7/19/18.
//  Copyright © 2018 Michael Sun and Eric Frankel. All rights reserved.
//

import UIKit

class TitleViewController: UIViewController {
    
    
    @IBOutlet weak var distance: UITextField!
    @IBOutlet weak var time: UITextField!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        guard let identifier = segue.identifier else { return }
        
        if identifier == "mapShow" {
            
            let destination = segue.destination as! MapViewController
            if let distanceDouble = Double(distance.text!), let timeDouble = Double(time.text!) {
                
                destination.distance = distanceDouble
                destination.time = timeDouble
                
                
            }
            
        }
        
    }


}

