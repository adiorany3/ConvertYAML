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
1. `AKUN-001-UNKNOWN-VLESS-WS-123MS` (url=257ms, nekobox=291ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-130MS` (url=261ms, nekobox=280ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-122MS` (url=261ms, nekobox=293ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-128MS` (url=265ms, nekobox=301ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-131MS` (url=268ms, nekobox=299ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-132MS` (url=264ms, nekobox=288ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-134MS` (url=266ms, nekobox=297ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-136MS` (url=287ms, nekobox=310ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-122MS` (url=270ms, nekobox=288ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-132MS` (url=260ms, nekobox=291ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-144MS` (url=309ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-136MS` (url=308ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-134MS` (url=274ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-147MS` (url=275ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-154MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-132MS` (url=277ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-140MS` (url=282ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-131MS` (url=309ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-142MS` (url=270ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-274MS` (url=403ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-341MS` (url=3142ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-291MS` (url=566ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-365MS` (url=2991ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-371MS` (url=789ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-368MS` (url=888ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
