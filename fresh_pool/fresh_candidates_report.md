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
1. `AKUN-001-ORACLE-VLESS-WS-68MS` (url=214ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=214ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=221ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=210ms, nekobox=235ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-94MS` (url=221ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=225ms, nekobox=236ms, status=yes)
7. `AKUN-007-DIGITALOCEAN-VLESS-WS-91MS` (url=214ms, nekobox=233ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=223ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=213ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=232ms, nekobox=239ms, status=yes)
11. `AKUN-012-466688-VLESS-WS-107MS` (url=218ms, status=HTTP 204)
12. `AKUN-013-MYBB-VLESS-WS-86MS` (url=226ms, status=HTTP 204)
13. `AKUN-014-ADF-VLESS-WS-111MS` (url=224ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-71MS` (url=227ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-139MS` (url=222ms, status=HTTP 204)
16. `AKUN-017-PAGES-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
17. `AKUN-018-MEDIUM-VLESS-WS-80MS` (url=223ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-97MS` (url=219ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-152MS` (url=220ms, status=HTTP 204)
20. `AKUN-021-DEV-VLESS-WS-174MS` (url=2114ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-148MS` (url=205ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-123MS` (url=247ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-251MS` (url=578ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-228MS` (url=540ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-243MS` (url=496ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
