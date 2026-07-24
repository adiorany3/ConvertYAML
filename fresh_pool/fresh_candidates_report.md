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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-129MS` (url=276ms, nekobox=296ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-131MS` (url=262ms, nekobox=284ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-121MS` (url=261ms, nekobox=305ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-132MS` (url=269ms, nekobox=302ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-130MS` (url=261ms, nekobox=289ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-136MS` (url=265ms, nekobox=296ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-139MS` (url=308ms, nekobox=296ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS` (url=268ms, nekobox=292ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-136MS` (url=270ms, nekobox=292ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-135MS` (url=270ms, nekobox=295ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-140MS` (url=294ms, status=HTTP 204)
12. `AKUN-012-008500-VLESS-WS-140MS` (url=269ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-141MS` (url=267ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-135MS` (url=272ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-144MS` (url=251ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=277ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-140MS` (url=304ms, status=HTTP 204)
18. `AKUN-018-CCWU-VLESS-WS-133MS` (url=259ms, status=HTTP 204)
19. `AKUN-019-ZOOM-VLESS-WS-142MS` (url=291ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-142MS` (url=274ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-186MS` (url=306ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-196MS` (url=314ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-189MS` (url=279ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-134MS` (url=281ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-211MS` (url=387ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
