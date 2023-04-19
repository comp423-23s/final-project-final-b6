import { Component } from '@angular/core';
import { ActivatedRoute} from '@angular/router';
import { Observable } from 'rxjs';
import {MemberService, User} from './members.service';
import { PermissionService } from 'src/app/permission.service';
import { MatDialog } from '@angular/material/dialog';


@Component({
  selector: 'app-members',
  templateUrl: './members.component.html',
  styleUrls: ['./members.component.css']
})
export class MembersComponent {
  public members$: Observable<User[]>;
  public adminPermission$: Observable<boolean>;


  constructor(
    private memberService: MemberService,
    private route: ActivatedRoute,
    private permission: PermissionService,
    protected deleteDialog: MatDialog,){
      this.adminPermission$ = this.permission.check('admin.view', 'admin/')
      const routeParams = this.route.snapshot.paramMap;
      this.members$ = memberService.getMembers(String(routeParams.get('organizationName')));
    }
}