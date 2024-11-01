import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'weather-details',
  templateUrl: './weatherDetails.component.html',
  styleUrls: ['./weatherDetails.component.scss']
})

export class WeatherDetails implements OnInit {
  @Input() weatherData: data[];
  city: string;
  cityWeather: data;

  ngOnInit() {

  }

  getCityWeather(event: Event) {
    this.city = (<HTMLInputElement>event.target).value;
    this.cityWeather = this.weatherData.find((weather) => {
      return weather.name.toLowerCase() === this.city.toLowerCase();
    });
  }
}

interface data {
  name: string;
  temperature: string;
  wind: string;
  humidity: string;
}