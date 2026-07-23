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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-116MS` (url=241ms, nekobox=273ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-120MS` (url=254ms, nekobox=275ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-126MS` (url=275ms, nekobox=289ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-124MS` (url=242ms, nekobox=283ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-122MS` (url=255ms, nekobox=291ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=247ms, nekobox=280ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-123MS` (url=250ms, nekobox=292ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS` (url=263ms, nekobox=288ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=255ms, nekobox=295ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-135MS` (url=261ms, nekobox=285ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-125MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-008500-VLESS-WS-139MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-134MS` (url=241ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-141MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=248ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-160MS` (url=281ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-125MS` (url=260ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-131MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-123MS` (url=249ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-145MS` (url=269ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-153MS` (url=272ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-151MS` (url=282ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-133MS` (url=250ms, status=HTTP 204)
24. `AKUN-024-ZVC-VLESS-WS-150MS` (url=264ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-138MS` (url=260ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
