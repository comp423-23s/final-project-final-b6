import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';
import { ReturnStatement } from '@angular/compiler';

export interface Event {
  id: number;
  name: string;
  description: string;
  date_time: Date;
  location: string;
  image: string;
  organization_id: number;
}

@Injectable({
  providedIn: 'root'
})

export class OrganizationDetailsService {
  datasource: Event[] = [];
  constructor(private http: HttpClient) { }

  getOrganizationEvents(organizationName: string): Observable<Event[]>{
    return this.http.get<Event[]>(`api/${organizationName}/events`)
  }
}


