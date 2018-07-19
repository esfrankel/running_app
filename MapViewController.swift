//
//  MapViewController.swift
//  aiRun
//
//  Created by Michael Sun on 7/19/18.
//  Copyright © 2018 Michael Sun and Eric Frankel. All rights reserved.
//

import UIKit
import MapKit
import GoogleMaps
import GooglePlaces

class MapViewController: UIViewController {
    
    var distance: Double!
    var time: Double!
    var locationManager = CLLocationManager()
    var mapView = GMSMapView()
    var marker = GMSMarker()
    var path = GMSMutablePath()
    var coordinates: [CLLocationCoordinate2D] = [] {
        didSet {
            
            
            
            path.add(coordinates.last!)
            let polyline = GMSPolyline(path: path)
            polyline.map = mapView
            view = mapView
            
            
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.requestWhenInUseAuthorization()
        locationManager.requestLocation()
        
        if let location = locationManager.location {
            
            coordinates.append(CLLocationCoordinate2D(latitude: location.coordinate.latitude, longitude: location.coordinate.longitude))
            let camera = GMSCameraPosition.camera(withLatitude: coordinates.last!.latitude, longitude: coordinates.last!.longitude, zoom: 16.0)
            mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
            marker = GMSMarker(position: coordinates.last!)
            marker.title = "Current"
            marker.snippet = "Location"
            marker.map = mapView
            view = mapView
            
            coordinates.append(CLLocationCoordinate2D(latitude: location.coordinate.latitude + 5, longitude: location.coordinate.longitude + 5))
            
        }
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}

extension MapViewController: CLLocationManagerDelegate {
    
    
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        print("error:: \(error.localizedDescription)")
    }
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        if status == .authorizedWhenInUse {
            locationManager.requestLocation()
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        
        if let location = locations.last {
            
            coordinates.append(location.coordinate)
            let camera = GMSCameraPosition.camera(withLatitude: coordinates.last!.latitude, longitude: coordinates.last!.longitude, zoom: 10.0)
            mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
            
        }
        
    }
}



