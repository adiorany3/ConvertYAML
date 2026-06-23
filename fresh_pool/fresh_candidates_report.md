# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-95MS` (url=258ms, nekobox=345ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=319ms, nekobox=359ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-98MS` (url=318ms, nekobox=296ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-123MS` (url=242ms, nekobox=350ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-123MS` (url=271ms, nekobox=354ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-128MS` (url=245ms, nekobox=271ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-138MS` (url=313ms, nekobox=272ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-146MS`
10. `AKUN-010-VULTR-VLESS-WS-140MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-134MS` (url=246ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-324MS` (url=710ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-337MS` (url=700ms, status=HTTP 204)
14. `AKUN-015-OPENAI-VLESS-WS-126MS` (url=316ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-336MS` (url=755ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-317MS` (url=744ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-297MS` (url=822ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-377MS` (url=695ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-107MS` (url=236ms, status=HTTP 204)
20. `AKUN-026-APPLESERAJ-VLESS-WS-567MS` (url=811ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-594MS` (url=1013ms, status=HTTP 204)
22. `AKUN-030-CLOUDFLARE-VLESS-WS-621MS` (url=894ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-646MS` (url=1105ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
