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
1. `AKUN-001-VULTR-VLESS-WS-130MS` (url=262ms, nekobox=312ms, status=yes)
2. `AKUN-002-NET-NL-VLESS-WS-132MS` (url=250ms, nekobox=295ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-134MS` (url=262ms, nekobox=293ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-134MS` (url=252ms, nekobox=302ms, status=yes)
5. `AKUN-005-SPACECORE-VLESS-WS-130MS` (url=253ms, nekobox=299ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-141MS` (url=297ms, nekobox=318ms, status=yes)
7. `AKUN-007-HOSTOFF-NET-VLESS-WS-135MS` (url=257ms, nekobox=308ms, status=yes)
8. `AKUN-008-NETCUP-VLESS-WS-136MS` (url=256ms, nekobox=302ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-132MS` (url=261ms, nekobox=306ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS` (url=280ms, nekobox=287ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-148MS` (url=259ms, status=HTTP 204)
12. `AKUN-012-U1HOST-FRA-VLESS-WS-142MS` (url=251ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-150MS` (url=246ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-152MS` (url=263ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-146MS` (url=291ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-156MS` (url=281ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-146MS` (url=264ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-147MS` (url=289ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-361MS` (url=710ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-358MS` (url=690ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-385MS` (url=781ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-383MS` (url=761ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-380MS` (url=781ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-381MS` (url=806ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-366MS` (url=685ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
