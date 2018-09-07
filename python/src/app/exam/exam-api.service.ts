import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {API_URL} from '../env';
import {Exam} from './exam.model';

const httpOptions = {
    headers: new HttpHeaders({
        'Content-Type':'application/json'
    })
};

@Injectable()
export class ExamsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http
      .get<Exam[]>(`${API_URL}/exams`)

  }

  postExams(exam: Exam): Observable<Exam> {
    return this.http.post<Exam>(`${API_URL}`, exam, httpOptions)
  }
}
