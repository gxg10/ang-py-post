import { Component, OnInit, OnDestroy } from '@angular/core';
import {Subscription} from 'rxjs/';
import {ExamsApiService} from './exam/exam-api.service';
import {Exam} from './exam/exam.model';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  examListSubs: Subscription;
  examList: Exam[];
  // test = '
  //   'title': "TypeScript Advanced Exam",
  //   'description': "Tricky questions about TypeScript."
  // ';

  constructor(private ExamsApi: ExamsApiService) {

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
  }

  // postex() {
  //   this.ExamsApi.postExams(this.exam)
  // }
}