import { Component, OnInit, OnDestroy, ElementRef } from '@angular/core';
import {Subscription} from 'rxjs/';
import {ExamsApiService} from './exam/exam-api.service';
import {Exam} from './exam/exam.model';
import { Customer } from './customers/customer';
import { CustomerService } from './customers/customers.service';
import { OrderService } from './orders/orders.service';
import { Orders } from './orders/orders.model';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';

import {FormControl} from '@angular/forms';

import { NativeDateAdapter, DateAdapter, MAT_DATE_FORMATS } from '@angular/material';
import { AppDateAdapter, APP_DATE_FORMATS} from './date.adapter';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';


const URL = 'http://127.0.0.1:5000/txtupload';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [
    {
      provide: DateAdapter, useClass: AppDateAdapter
  },
  {
      provide: MAT_DATE_FORMATS, useValue: APP_DATE_FORMATS
  }
  ]
})

export class AppComponent implements OnInit, OnDestroy {

  title = 'app';
  examListSubs: Subscription;
  custListSubs: Subscription;
  examList: Exam[];
  custList: Customer[];
  orderList: Orders[];
  // data = ['val1', 'val2', 'val3'];
  // filtered = this.data;
  event: MatDatepickerInputEvent<Date>;
  data;

  filestoUpload: Array<File> = [];
  mesaj_upload;

  constructor(private ExamsApi: ExamsApiService,
    private CustApi: CustomerService,
    private OrdersApi: OrderService,
    private el: ElementRef,
    private http: HttpClient) {

  }

  // search(val: any) {
  //   if (!val) { this.filtered = this.data; }
  //   this.filtered = this.data.filter(d =>d.indexOf(val)>=0);
  // }

  ngOnInit() {
    this.examListSubs = this.ExamsApi
    .getExams()
    .subscribe(
      res => {
        console.log(res);
        this.examList = res;
      },
      console.error
    );

  }

  ngOnDestroy() {
    this.examListSubs.unsubscribe();
    this.custListSubs.unsubscribe();
  }

  getC() {
    this.CustApi.getCustomers()
      .subscribe(
        res => {
          console.log(res);
          this.custList = res;
        }
      );
  }

  getOr() {
    this.OrdersApi.getOrders()
    .subscribe(
      res => {
        console.log(res);
        this.orderList = res;
      }
    );
  }

  addEvent(type: string, event: MatDatepickerInputEvent<Date>) {
    const date = event.targetElement as HTMLInputElement;
    // console.log(event.value);
    this.data = date.value;
    // this.data = 'AL';
    console.log(this.data);
  }


  // getOrder(id) {
  //   this.OrdersApi.getOrdersById(id)
  //   .subscribe(
  //     res => {
  //       this.orderList = res;
  //       console.log(res);
  //     }
  //   );
  // }

  getOrdByDate(data) {
    this.OrdersApi.getOrdersByDate(data)
    .subscribe(
      res => {
        this.orderList = res;
        console.log(res);
      }
    );
  }

  upload() {
    // locate the file element meant for the file upload.
        const inputEl: HTMLInputElement = this.el.nativeElement.querySelector('#photo');
        const files: Array<File> = this.filestoUpload;
        console.log(files);
    // get the total amount of files attached to the file input.
        const fileCount: number = inputEl.files.length;
    // create a new fromdata instance
        const formData = new FormData();
    // check if the filecount is greater than zero, to be sure a file was selected.
        if (fileCount > 0) { // a file was selected
            // append the key name 'photo' with the first file in the element
            for (let i = 0; i < fileCount; i++) {
                formData.append('txtFileFilter', inputEl.files.item(i));
            }
            // call the angular http method
            this.http
                .post(URL, formData).pipe(map((res:any) => res)).subscribe(
                 (res) => {
                    this.mesaj_upload = res;
                    return console.log('files', res);
                 });
            this.filestoUpload = undefined;
          }
       }

  // getdate(newdate) {
  //   this.OrdersApi.getOrdersByDate(newdate)
  //   .subscribe(
  //     res => {
  //       console.log(res);
  //     }
  //   );
  // }

  // postex() {
  //   this.ExamsApi.postExams(this.exam)
  // }
}