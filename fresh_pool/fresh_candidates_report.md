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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS` (url=306ms, nekobox=232ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-105MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-120MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-127MS`
5. `AKUN-004-OVH-VLESS-WS-123MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS`
8. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-135MS`
9. `AKUN-008-PUBLICDOMAINREGISTRY-NET-VLESS-WS-133MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-127MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-137MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-151MS` (url=331ms, status=HTTP 204)
13. `AKUN-013-1PASSWORD-VLESS-WS-121MS` (url=275ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-135MS` (url=278ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-167MS` (url=316ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-153MS` (url=310ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-144MS` (url=290ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-174MS` (url=320ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-152MS` (url=302ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-205MS` (url=583ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-136MS` (url=308ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-177MS` (url=384ms, status=HTTP 204)
23. `AKUN-023-466688-VLESS-WS-138MS` (url=313ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-261MS` (url=1115ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-300MS` (url=724ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
