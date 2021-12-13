import { HttpClient } from '@angular/common/http';
import { AfterViewInit } from '@angular/core';
import { Component, ViewChild } from '@angular/core';
import { GoogleMap, MapCircle } from '@angular/google-maps'
import { Observable } from 'rxjs';
import { Pokemon } from './models/pokemon.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Pokemon';
  center: google.maps.LatLngLiteral = { lat: 35.5062897, lng: 138.6484981};
  zoom = 12;
  obsCiVett : Observable<Pokemon[]>;

  constructor(public http: HttpClient){}

  Tana(): void {
    console.log('ciao')
    this.obsCiVett = this.http.get<Pokemon[]>("http://127.0.0.1:5000/all");
    this.obsCiVett.subscribe(this.PrepData);
  }

  markerList: google.maps.MarkerOptions[];

  PrepData = (data: Pokemon[]) => {
    console.log(data)
    this.markerList = [];
    for (const i of data['pokemon']) {
      let m: google.maps.MarkerOptions = {
        position: new google.maps.LatLng(i.lat, i.lng),
        icon: this.findImage()
      }
      this.markerList.push(m)
    }
  }

  findImage() {
    return { url: './assets/img/hole.png', scaledSize: new google.maps.Size(32,32) };
  }

  //fine primo punto

}
