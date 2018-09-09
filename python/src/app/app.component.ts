import { Component, OnInit, OnDestroy } from '@angular/core';
import {Subscription} from 'rxjs/';
import {ExamsApiService} from './exam/exam-api.service';
import {Exam} from './exam/exam.model';
import { Customer } from './customers/customer';
import { CustomerService } from './customers/customers.service';
import { OrderService } from './orders/orders.service';
import { Orders } from './orders/orders.model';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  examListSubs: Subscription;
  custListSubs: Subscription;
  examList: Exam[];
  custList: Customer[];
  orderList: Orders[];
  id = 270168;
  // data = ['val1', 'val2', 'val3'];
  // filtered = this.data;

  data: Date ;
  events: string[] = [];

  constructor(private ExamsApi: ExamsApiService,
    private CustApi: CustomerService,
    private OrdersApi: OrderService) {

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
    // this.events.push('${type}:${event.value}');
    // this.data = event.value;
    this.data = event.targetElement.value;
    // console.log(event.targetElement.value);
    console.log(this.data);
  }

  getOrder(id) {
    this.OrdersApi.getOrdersById(id)
    .subscribe(
      res => {
        this.orderList = res;
        console.log(res);
      }
    );
  }


  

  // postex() {
  //   this.ExamsApi.postExams(this.exam)
  // }
}