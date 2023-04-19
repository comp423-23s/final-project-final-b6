import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';

export interface User {
  id: number;
  pid: number;
  onyen: string;
  first_name: string;
  last_name: string;
  email: string;
  pronouns: string;
  permissions: [];
}

@Injectable({
  providedIn: 'root'
})

export class MemberService {
  apiBaseUrl = "/api";
  organizations: User[] = [];

  constructor(private http: HttpClient) { }

  getMembers(organizationName: String): Observable<User[]> {
    return this.http.get<User[]>(`/api/${organizationName}/members`);
  }
}
