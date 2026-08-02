# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
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
1. `AKUN-001-LEVIKOGJGFDD-VLESS-WS-86MS` (url=210ms, nekobox=236ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-86MS` (url=231ms, nekobox=244ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-90MS` (url=211ms, nekobox=262ms, status=yes)
4. `AKUN-004-877774-VLESS-WS-106MS` (url=239ms, nekobox=241ms, status=yes)
5. `AKUN-005-SPEEDTEST-VLESS-WS-113MS` (url=215ms, nekobox=196ms, status=no)
6. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-102MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-122MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-128MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-142MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-174MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-184MS`
12. `AKUN-012-RMGYVPN-VLESS-WS-315MS` (url=662ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-144MS` (url=306ms, status=HTTP 204)
14. `AKUN-016-SUKARIO-VLESS-WS-627MS` (url=1043ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-548MS` (url=1103ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-557MS` (url=1077ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-680MS` (url=1114ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-680MS` (url=1110ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-687MS` (url=1102ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-717MS` (url=1120ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-793MS` (url=1235ms, status=HTTP 204)
22. `AKUN-029-UNKNOWN-VLESS-WS-749MS` (url=1286ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-801MS` (url=1302ms, status=HTTP 204)
24. `AKUN-031-UNKNOWN-VLESS-WS-776MS` (url=1239ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-830MS` (url=2084ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
