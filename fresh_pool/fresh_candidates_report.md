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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=558ms, nekobox=251ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-66MS` (url=223ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=213ms, nekobox=254ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-65MS` (url=229ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=207ms, nekobox=242ms, status=yes)
6. `AKUN-006-PUBLICDOMAINREGISTRY-NET-VLESS-WS-76MS` (url=203ms, nekobox=252ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-80MS` (url=219ms, nekobox=244ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-64MS` (url=214ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=223ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=214ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-106MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-72MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-114MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-169MS` (url=315ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-71MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-68MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-76MS` (url=201ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-232MS` (url=522ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-66MS` (url=229ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-87MS` (url=250ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-234MS` (url=489ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-350MS` (url=741ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
