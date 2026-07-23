# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-UNKNOWN-VLESS-WS-116MS` (url=290ms, nekobox=275ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-119MS` (url=258ms, nekobox=288ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-126MS` (url=256ms, nekobox=297ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-127MS` (url=290ms, nekobox=282ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS` (url=249ms, nekobox=288ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-134MS` (url=288ms, nekobox=294ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-138MS` (url=255ms, nekobox=291ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-141MS` (url=272ms, nekobox=339ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-150MS` (url=294ms, nekobox=275ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-128MS` (url=250ms, nekobox=288ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=279ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-159MS` (url=261ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-170MS` (url=389ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-158MS` (url=296ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-192MS` (url=364ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-219MS` (url=317ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-133MS` (url=322ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-127MS` (url=277ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-180MS` (url=300ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-432MS` (url=857ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-433MS` (url=1583ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-619MS` (url=794ms, status=HTTP 204)
23. `AKUN-034-CLOUDFLARE-VLESS-WS-794MS` (url=2001ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-897MS` (url=1474ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
