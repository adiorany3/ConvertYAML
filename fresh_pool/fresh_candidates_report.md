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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=208ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=207ms, nekobox=243ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-74MS` (url=214ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=205ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=206ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=208ms, nekobox=252ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-63MS` (url=201ms, nekobox=231ms, status=yes)
8. `AKUN-008-WEYRO-NET-VLESS-WS-74MS` (url=206ms, nekobox=234ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-75MS` (url=196ms, nekobox=233ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, nekobox=234ms, status=yes)
11. `AKUN-011-SSL-1134-VLESS-WS-84MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-80MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-81MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-SIN-VLESS-WS-71MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-77MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-73MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-1PASSWORD-VLESS-WS-78MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-76MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-103MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-86MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-PAGES-VLESS-WS-120MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-180MS` (url=386ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-227MS` (url=482ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-224MS` (url=484ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-244MS` (url=529ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
