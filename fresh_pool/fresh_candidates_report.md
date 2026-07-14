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
1. `AKUN-001-UNKNOWN-VLESS-WS-97MS` (url=351ms, nekobox=325ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-98MS` (url=296ms, nekobox=381ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-99MS` (url=375ms, nekobox=383ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-106MS` (url=348ms, nekobox=340ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=372ms, nekobox=385ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-110MS` (url=348ms, nekobox=556ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-97MS` (url=357ms, nekobox=380ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-99MS` (url=340ms, nekobox=417ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-106MS` (url=422ms, nekobox=369ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=310ms, nekobox=407ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-102MS` (url=368ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-123MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=352ms, status=HTTP 204)
14. `AKUN-014-PUBLICDOMAINREGISTRY-NET-VLESS-WS-117MS` (url=325ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-119MS` (url=446ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=316ms, status=HTTP 204)
17. `AKUN-017-SHOPIFY-VLESS-WS-121MS` (url=336ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-96MS` (url=333ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-117MS` (url=365ms, status=HTTP 204)
20. `AKUN-020-MEDIUM-VLESS-WS-105MS` (url=357ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-114MS` (url=373ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-127MS` (url=338ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-108MS` (url=330ms, status=HTTP 204)
24. `AKUN-024-ES-FORNEX-20160629-VLESS-WS-136MS` (url=385ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-109MS` (url=355ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
