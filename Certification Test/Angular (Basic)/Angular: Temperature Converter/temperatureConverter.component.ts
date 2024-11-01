import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'temperature-converter',
  templateUrl: './temperatureConverter.component.html',
  styleUrls: ['./temperatureConverter.component.scss']
})

export class TemperatureConverter implements OnInit {
  celsius: number = 0;
  fahrenheit: number = 0;

  ngOnInit() {
    // C = (F − 32) × 5/9
    // F = C*9/5 + 32
 
 }

  onCelsiusChange(celsius: string) {
    this.celsius = parseFloat(celsius);
    this.fahrenheit = this.celsius * 9 / 5 + 32;
    this.fahrenheit = parseFloat(this.fahrenheit.toFixed(1));
  }

  onFahrenheitChange(fahrenheit: string) {
    this.fahrenheit = parseFloat(fahrenheit);
    this.celsius = (this.fahrenheit - 32) * 5 / 9;
    this.celsius = parseFloat(this.celsius.toFixed(1));
  }
}
