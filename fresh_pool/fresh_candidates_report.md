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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=216ms, nekobox=239ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-74MS` (url=203ms, nekobox=244ms, status=yes)
3. `AKUN-003-DIGITALOCEAN-VLESS-WS-92MS` (url=227ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=219ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-102MS` (url=257ms, nekobox=241ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=230ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=242ms, nekobox=251ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-95MS` (url=221ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=216ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS` (url=225ms, nekobox=245ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-88MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-106MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-88MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-106MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-96MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-114MS` (url=201ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-107MS` (url=201ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-87MS` (url=223ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-90MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-130MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-105MS` (url=229ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-140MS` (url=206ms, status=HTTP 204)
24. `AKUN-024-PAGES-VLESS-WS-122MS` (url=231ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-223MS` (url=514ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
