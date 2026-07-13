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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-92MS` (url=289ms, nekobox=351ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS` (url=372ms, nekobox=330ms, status=yes)
3. `AKUN-003-DIGITALOCEAN-VLESS-WS-103MS` (url=299ms, nekobox=336ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=294ms, nekobox=400ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-102MS` (url=301ms, nekobox=335ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-120MS` (url=340ms, nekobox=357ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-105MS` (url=325ms, nekobox=331ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS` (url=323ms, nekobox=333ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS` (url=311ms, nekobox=325ms, status=yes)
10. `AKUN-010-DE-XTOM-20190821-VLESS-WS-114MS` (url=290ms, nekobox=338ms, status=yes)
11. `AKUN-012-ZVC-VLESS-WS-115MS` (url=418ms, status=HTTP 204)
12. `AKUN-013-HETZNER-VLESS-WS-129MS` (url=332ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-152MS` (url=289ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-121MS` (url=295ms, status=HTTP 204)
15. `AKUN-016-ZOOM-VLESS-WS-134MS` (url=304ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-160MS` (url=347ms, status=HTTP 204)
17. `AKUN-018-SHOPIFY-VLESS-WS-143MS` (url=320ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-240MS` (url=441ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-141MS` (url=339ms, status=HTTP 204)
20. `AKUN-021-US-VLESS-WS-107MS` (url=296ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-321MS` (url=727ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-327MS` (url=762ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-299MS` (url=696ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-332MS` (url=680ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-306MS` (url=632ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
