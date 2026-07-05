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
1. `AKUN-001-UNKNOWN-VLESS-WS-88MS` (url=229ms, nekobox=243ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-97MS` (url=230ms, nekobox=243ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-112MS` (url=257ms, nekobox=273ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS` (url=206ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-110MS` (url=228ms, nekobox=217ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-106MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS` (url=226ms, nekobox=251ms, status=yes)
11. `AKUN-010-WEYRO-NET-VLESS-WS-126MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-132MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-148MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-153MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-130MS` (url=245ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-130MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-124MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-303MS` (url=350ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-371MS` (url=779ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-367MS` (url=750ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-347MS` (url=613ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-417MS` (url=847ms, status=HTTP 204)
23. `AKUN-024-CELESTARA-VLESS-WS-412MS` (url=854ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-417MS` (url=890ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-147MS` (url=221ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
