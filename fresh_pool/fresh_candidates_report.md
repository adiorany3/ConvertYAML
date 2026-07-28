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
1. `AKUN-001-CL-65-49-192-0-19-VLESS-WS-81MS`
2. `AKUN-003-CLOUDFLARE-VLESS-WS-113MS` (url=203ms, nekobox=193ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-130MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-149MS` (url=225ms, nekobox=202ms, status=no)
6. `AKUN-004-UNKNOWN-VLESS-WS-91MS`
7. `AKUN-005-UNKNOWN-VLESS-WS-95MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-103MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-116MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-99MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-82MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=243ms, nekobox=221ms, status=no)
13. `AKUN-010-UNKNOWN-VLESS-WS-145MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-119MS` (url=278ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=242ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-245MS` (url=551ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-349MS` (url=800ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-355MS` (url=2011ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-166MS` (url=399ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-370MS` (url=3912ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-80MS` (url=788ms, status=HTTP 204)
22. `AKUN-024-SUKARIO-VLESS-WS-624MS` (url=1051ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-550MS` (url=538ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-689MS` (url=3539ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-809MS` (url=1216ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
