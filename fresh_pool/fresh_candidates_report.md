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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=235ms, nekobox=277ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-67MS` (url=234ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=233ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=249ms, nekobox=7180ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-64MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-007-CZ-LOTUNA-19970206-VLESS-WS-81MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-70MS`
10. `AKUN-009-ZVC-VLESS-WS-92MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-70MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-84MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-95MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-85MS` (url=282ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-108MS` (url=238ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-75MS` (url=269ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-88MS` (url=241ms, status=HTTP 204)
21. `AKUN-021-TENCENT-VLESS-WS-86MS` (url=232ms, status=HTTP 204)
22. `AKUN-022-WEBEX-VLESS-WS-111MS` (url=275ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-137MS` (url=276ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-251MS` (url=553ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-275MS` (url=3648ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
