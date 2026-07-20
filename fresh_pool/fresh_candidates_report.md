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
1. `AKUN-001-UNKNOWN-VLESS-WS-94MS` (url=243ms, nekobox=244ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-94MS` (url=212ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=235ms, nekobox=258ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-97MS` (url=229ms, nekobox=7174ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-86MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-102MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-117MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-92MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-119MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-134MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-136MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-99MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=250ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-143MS` (url=277ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-129MS` (url=252ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-127MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-387MS` (url=776ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-401MS` (url=2325ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-413MS` (url=1172ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-680MS` (url=1097ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-738MS` (url=1233ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-719MS` (url=1115ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
