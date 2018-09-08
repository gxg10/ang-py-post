import { Component, OnInit, OnDestroy } from '@angular/core';
import {Subscription} from 'rxjs/';
import {ExamsApiService} from './exam/exam-api.service';
import {Exam} from './exam/exam.model';
import { Customer } from './customers/customer';
import { CustomerService } from './customers/customers.service';
import { OrderService } from './orders/orders.service';
import { Orders } from './orders/orders.model';


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
  // test = '
  //   'title': "TypeScript Advanced Exam",
  //   'description': "Tricky questions about TypeScript."
  // ';

  constructor(private ExamsApi: ExamsApiService,
    private CustApi: CustomerService,
    private OrdersApi: OrderService) {

  }

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
    )
  }

  

  // postex() {
  //   this.ExamsApi.postExams(this.exam)
  // }
}