import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  data1 = '';

  cite = 'interpolation';
  imagepath = 'https://upload.wikimedia.org/wikipedia/en/8/88/Peugeot_Logo.png';
  setup = 'what tis means';
  punchline = 'haloumi';
  status = true;

  male = {
    name: 'Brande George',
    sex: 'm',
    rating: 4,
    photo: 'https://upload.wikimedia.org/wikipedia/en/8/88/Peugeot_Logo.png'
  };

  female = {
    name: 'Doe Girl',
    sex: 'f',
    rating: '5',
    photo: 'https://upload.wikimedia.org/wikipedia/commons/8/8c/Peugeot_RCZ_%28Facelift%29_%E2%80%93_Frontansicht%2C_7._Dezember_2014%2C_Ratingen.jpg'
  };

  person: any = this.female;

  star = false;

  get symbol(): string {
    return this.star ? '&#10032;' : '&#10003;';
  }

  rating(count: number): string {
    return 'Your current rating is ' + count;
  }



  constructor() { }


  ngOnInit() {
  }

  // pushHide() {

  //     if (this.status === false) {
  //       this.status = true;
  //     } else {
  //       this.status = false;
  //     }
  //   }
  }

