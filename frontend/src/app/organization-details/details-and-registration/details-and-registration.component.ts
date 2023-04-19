import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { OrganizationService } from 'src/app/organizations/organizations.service';
import { Organization } from 'src/app/organizations/organizations.service';
import { MemberService, User } from '../members/members.service';
import { ProfileService, Profile } from 'src/app/profile/profile.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatDialog } from '@angular/material/dialog';
import { LeaveDialogComponent } from './leave-dialog/leave-dialog.component'


@Component({
  selector: 'app-details-and-registration',
  templateUrl: './details-and-registration.component.html',
  styleUrls: ['./details-and-registration.component.css']
})

export class DetailsAndRegistrationComponent {
  public organizationName: String;
  public organization$: Observable<Organization>;
  public isMember: boolean;
  public profile$: Observable<Profile | undefined>;

  constructor(
    private organizationService: OrganizationService,
    private route: ActivatedRoute,
    private profileService: ProfileService,
    private memberService: MemberService,
    protected deleteDialog: MatDialog,
    protected snackBar: MatSnackBar) {
    const routeParams = this.route.snapshot.paramMap;
    this.profile$ = profileService.profile$;
    this.organizationName = String(routeParams.get('organizationName'));
    this.organization$ = organizationService.getOrganizationDetails(String(routeParams.get('organizationName')));
    this.isMember = false;
    this.memberService.getMembers(String(routeParams.get('organizationName'))).subscribe((members) => { this.getIsMember(members); })
  }

  getIsMember(members: User[]) {
    this.profile$.subscribe(
      (profile) => {
        for (let member of members) {
          if (profile) { if (member.id == profile.id) { this.isMember = true; } }
        }
      })
  }

  handleJoin() {
    this.profile$.subscribe(
      (profile) => {
        if (profile) {
          let user: User = {
            "id": profile.id ?? 0, "pid": profile.pid ?? 0, "onyen": profile.onyen ?? "", "first_name": profile.first_name ?? "",
            "last_name": profile.last_name ?? "", "email": profile.email ?? "", "pronouns": profile.pronouns ?? "", "permissions": profile.permissions
          };
          this.memberService.addMember(this.organizationName, user).subscribe((user) => { this.onJoinSuccess(user) });
        }
      })
  }

  private onJoinSuccess(user: User) {
    this.snackBar.open(`Successfully Joined ${this.organizationName}!`, "", { duration: 2000 });
    this.isMember = true;
  }

  private onLeaveSuccess(user: User){
    this.snackBar.open(`Successfully Left ${this.organizationName}!`, "", { duration: 2000 });
    this.isMember = false;
  }

  deleteMember() {
    this.profile$.subscribe(
      (profile) => {
        if (profile) {
          let user: User = {
            "id": profile.id ?? 0, "pid": profile.pid ?? 0, "onyen": profile.onyen ?? "", "first_name": profile.first_name ?? "",
            "last_name": profile.last_name ?? "", "email": profile.email ?? "", "pronouns": profile.pronouns ?? "", "permissions": profile.permissions
          };
          let dialogRef = this.deleteDialog.open(LeaveDialogComponent, { data: { "organizationName": this.organizationName, "user": user } });
          dialogRef.afterClosed().subscribe(() => {
          this.onLeaveSuccess(user);
          })
        }
      })
  }
}