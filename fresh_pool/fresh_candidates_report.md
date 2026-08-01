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
1. `AKUN-001-877774-VLESS-WS-79MS` (url=308ms, nekobox=276ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-79MS` (url=312ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=260ms, nekobox=296ms, status=yes)
4. `AKUN-004-SM-VLESS-WS-78MS` (url=314ms, nekobox=408ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=323ms, nekobox=314ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=300ms, nekobox=373ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=274ms, nekobox=275ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=278ms, nekobox=301ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-93MS` (url=322ms, nekobox=390ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-111MS` (url=331ms, nekobox=397ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-99MS` (url=317ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=366ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-110MS` (url=272ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-105MS` (url=273ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-101MS` (url=275ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-101MS` (url=326ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=306ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-117MS` (url=253ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-73MS` (url=384ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-122MS` (url=433ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-205MS` (url=374ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-150MS` (url=299ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-157MS` (url=340ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-510MS` (url=837ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-487MS` (url=783ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
