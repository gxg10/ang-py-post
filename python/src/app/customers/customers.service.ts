import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import {API_URL} from '../env';
import {Customer} from './customer';

@Injectable()
export class CustomerService{
    constructor(private http: HttpClient) {

    }
    getCustomers(): Observable<Customer[]> {
        return this.http.get<Customer[]>(`${API_URL}/customers`)
    }
}