# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-64MS` (url=210ms, nekobox=231ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=215ms, nekobox=241ms, status=yes)
3. `AKUN-003-SPACECORE-VLESS-WS-70MS` (url=225ms, nekobox=263ms, status=yes)
4. `AKUN-004-U1HOST-FRA-VLESS-WS-72MS` (url=222ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=226ms, nekobox=249ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-75MS` (url=283ms, nekobox=249ms, status=yes)
7. `AKUN-007-HOSTOFF-NET-VLESS-WS-76MS` (url=209ms, nekobox=250ms, status=yes)
8. `AKUN-008-NETCUP-VLESS-WS-75MS` (url=202ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=200ms, nekobox=244ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=223ms, nekobox=229ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=204ms, status=HTTP 204)
12. `AKUN-012-NET-NL-VLESS-WS-81MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-82MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-172MS` (url=372ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-229MS` (url=499ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-244MS` (url=484ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-253MS` (url=587ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-251MS` (url=537ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-251MS` (url=547ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-255MS` (url=534ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-228MS` (url=537ms, status=HTTP 204)
22. `AKUN-024-SPEEDTEST-VLESS-WS-87MS` (url=208ms, status=HTTP 204)
23. `AKUN-035-UNKNOWN-VLESS-WS-475MS` (url=805ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
