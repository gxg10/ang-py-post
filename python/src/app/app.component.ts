import { Component, OnInit, OnDestroy } from '@angular/core';
import {Subscription} from 'rxjs/';
import {ExamsApiService} from './exam/exam-api.service';
import {Exam} from './exam/exam.model';
import { Customer } from './customers/customer';
import { CustomerService } from './customers/customers.service';


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
  // test = '
  //   'title': "TypeScript Advanced Exam",
  //   'description': "Tricky questions about TypeScript."
  // ';

  constructor(private ExamsApi: ExamsApiService,
    private CustApi: CustomerService) {

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
          console.log(res)
          this.custList = res;
        }
      );
  }

  

  // postex() {
  //   this.ExamsApi.postExams(this.exam)
  // }
}