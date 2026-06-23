# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=195ms, nekobox=247ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS` (url=215ms, nekobox=270ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=235ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS` (url=202ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=208ms, nekobox=193ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS`
9. `AKUN-008-BROADNNET-KR-VLESS-WS-89MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-361MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-417MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-428MS` (url=829ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-409MS` (url=862ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-379MS` (url=793ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-386MS` (url=740ms, status=HTTP 204)
16. `AKUN-020-UNKNOWN-VLESS-WS-718MS` (url=1023ms, status=HTTP 204)
17. `AKUN-025-VIDBOXCO-VLESS-WS-730MS` (url=1117ms, status=HTTP 204)
18. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-805MS` (url=5167ms, status=HTTP 204)
19. `AKUN-027-VIDBOXCO-VLESS-WS-765MS` (url=1047ms, status=HTTP 204)
20. `AKUN-028-VIDBOXCO-VLESS-WS-829MS` (url=1004ms, status=HTTP 204)
21. `AKUN-029-VIDBOXCO-VLESS-WS-770MS` (url=1049ms, status=HTTP 204)
22. `AKUN-030-VIDBOXCO-VLESS-WS-771MS` (url=1064ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
