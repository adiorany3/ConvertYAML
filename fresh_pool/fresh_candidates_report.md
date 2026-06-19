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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-128MS` (url=278ms, nekobox=448ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-133MS` (url=239ms, nekobox=307ms, status=yes)
3. `AKUN-003-156-246-89-0-156-246-89-VLESS-WS-129MS` (url=266ms, nekobox=290ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS` (url=267ms, nekobox=294ms, status=yes)
5. `AKUN-005-MEDIUM-VLESS-WS-134MS` (url=258ms, nekobox=298ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS` (url=246ms, nekobox=310ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-140MS` (url=286ms, nekobox=310ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-139MS` (url=272ms, nekobox=300ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-148MS` (url=244ms, nekobox=240ms, status=no)
10. `AKUN-009-EU-VLESS-WS-149MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-145MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-142MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-CLOUDWEBMANAGE-EU-FR-VLESS-WS-136MS` (url=265ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-147MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-141MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-144MS` (url=270ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-141MS` (url=279ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-138MS` (url=325ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-372MS` (url=802ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-391MS` (url=761ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-378MS` (url=3196ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-395MS` (url=749ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-544MS` (url=894ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-669MS` (url=1026ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
