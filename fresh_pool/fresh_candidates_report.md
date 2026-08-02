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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=194ms, nekobox=182ms, status=no)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=217ms, nekobox=179ms, status=no)
3. `AKUN-001-UNKNOWN-VLESS-WS-70MS`
4. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS`
5. `AKUN-003-UNKNOWN-VLESS-WS-82MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-95MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS`
13. `AKUN-014-UNKNOWN-VLESS-WS-121MS` (url=310ms, status=HTTP 204)
14. `AKUN-015-FASTVPSUS-IPV4-VLESS-WS-123MS` (url=220ms, status=HTTP 204)
15. `AKUN-016-RMGYVPN-VLESS-WS-272MS` (url=556ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-524MS` (url=630ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-618MS` (url=1014ms, status=HTTP 204)
18. `AKUN-021-SPEEDTEST-VLESS-WS-636MS` (url=747ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-653MS` (url=1092ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-674MS` (url=1098ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-656MS` (url=1076ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-731MS` (url=846ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-770MS` (url=1205ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-775MS` (url=1523ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-802MS` (url=1339ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
