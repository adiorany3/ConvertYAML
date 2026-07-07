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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=219ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=222ms, nekobox=260ms, status=yes)
3. `AKUN-003-DIGITALOCEAN-VLESS-WS-75MS` (url=225ms, nekobox=267ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-85MS` (url=211ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=227ms, nekobox=252ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-73MS` (url=206ms, nekobox=278ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=210ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS` (url=240ms, nekobox=271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=292ms, nekobox=288ms, status=yes)
10. `AKUN-010-OVH-VLESS-WS-93MS` (url=226ms, nekobox=250ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-PAGES-VLESS-WS-132MS` (url=298ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-69MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-70MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-83MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-106MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-131MS` (url=237ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-108MS` (url=256ms, status=HTTP 204)
20. `AKUN-021-SPEEDTEST-VLESS-WS-373MS` (url=781ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-342MS` (url=748ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-374MS` (url=815ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-182MS` (url=342ms, status=HTTP 204)
24. `AKUN-025-ADF-VLESS-WS-95MS` (url=238ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-373MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
