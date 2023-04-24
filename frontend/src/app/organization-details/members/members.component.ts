import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { MemberService, User } from './members.service';
import { PermissionService } from 'src/app/permission.service';
import { MatDialog } from '@angular/material/dialog';
import { ProfileService, Profile } from 'src/app/profile/profile.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MemberDeleteDialogComponent } from './member-delete-dialog/member-delete-dialog.component'



@Component({
  selector: 'app-members',
  templateUrl: './members.component.html',
  styleUrls: ['./members.component.css']
})
export class MembersComponent {
  public members$: Observable<User[]>;
  public adminPermission$: Observable<boolean>;
  public organizationName: String;
  public profile$: Observable<Profile | undefined>;


  constructor(
    private memberService: MemberService,
    private route: ActivatedRoute,
    private profileService: ProfileService,
    private permission: PermissionService,
    protected deleteDialog: MatDialog,
    protected snackBar: MatSnackBar) {
    this.adminPermission$ = this.permission.check('admin.view', 'admin/')
    const routeParams = this.route.snapshot.paramMap;
    this.organizationName = String(routeParams.get('organizationName'));
    this.members$ = memberService.getMembers(String(routeParams.get('organizationName')));
    this.profile$ = profileService.profile$;
  }

  private onRemoveSuccess(user: User) {
    this.snackBar.open(`Successfully removed ${user.first_name} ${user.last_name} from ${this.organizationName}!`, "", { duration: 2000 });
    this.members$ = this.memberService.getMembers(this.organizationName);
  }

  handleRemoveMember(member: User) {
    let dialogRef = this.deleteDialog.open(MemberDeleteDialogComponent, { data: { "organizationName": this.organizationName, "user": member } });
    dialogRef.afterClosed().subscribe(() => { this.onRemoveSuccess(member); })
  }

  getRoll() {
    
  }

}