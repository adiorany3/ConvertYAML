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
1. `AKUN-001-FMN5-RENTED-NET2-VLESS-WS-111MS` (url=411ms, nekobox=351ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-105MS` (url=284ms, nekobox=424ms, status=yes)
3. `AKUN-003-ZOOM-VLESS-WS-145MS` (url=343ms, nekobox=431ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-118MS` (url=289ms, nekobox=316ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-120MS` (url=339ms, nekobox=325ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-173MS` (url=505ms, nekobox=402ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-174MS` (url=336ms, nekobox=319ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-184MS` (url=443ms, nekobox=483ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-207MS` (url=397ms, nekobox=426ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-236MS` (url=406ms, nekobox=341ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-152MS` (url=297ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-114MS` (url=334ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-205MS` (url=354ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-283MS` (url=584ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-226MS` (url=504ms, status=HTTP 204)
16. `AKUN-017-090227-VLESS-WS-225MS` (url=362ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-300MS` (url=867ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-306MS` (url=427ms, status=HTTP 204)
19. `AKUN-021-CN-CF-VLESS-WS-374MS` (url=893ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-275MS` (url=477ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-394MS` (url=495ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-597MS` (url=1008ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-268MS` (url=352ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-611MS` (url=1061ms, status=HTTP 204)
25. `AKUN-030-SUKARIO-VLESS-WS-511MS` (url=868ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
