import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';
import { Permission } from 'src/app/profile/profile.service';

export interface User {
  id: number;
  pid: number;
  onyen: string;
  first_name: string;
  last_name: string;
  email: string;
  pronouns: string;
  permissions: Permission[];
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

  addMember(organizationName: String, user: User): Observable<User> {
    return this.http.post<User>(`/api/${organizationName}/members/add`, user);
  }

  deleteMember(organizationName: String, user: User) {
    const httpOptions: Object = {
      headers: new HttpHeaders({
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }),
      body: user,
    };
    return this.http.delete<User>(`/api/${organizationName}/members/delete`, httpOptions);
  }

}
