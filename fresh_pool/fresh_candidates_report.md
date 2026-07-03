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
1. `AKUN-001-ALIBABA-VLESS-WS-78MS` (url=215ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=249ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-81MS` (url=223ms, nekobox=245ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-69MS` (url=282ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=196ms, nekobox=250ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-76MS` (url=204ms, nekobox=234ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-85MS` (url=239ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=204ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=209ms, nekobox=234ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-74MS` (url=225ms, nekobox=242ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-89MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-IONIS-163-5-207-VLESS-WS-90MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-99MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-86MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-111MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-127MS` (url=198ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-130MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-99MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-66MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-74MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-228MS` (url=499ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-219MS` (url=501ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-241MS` (url=539ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-248MS` (url=524ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-78MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
