# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-156-246-93-0-156-246-93-VLESS-WS-130MS` (url=256ms, nekobox=291ms, status=yes)
2. `AKUN-002-CNAE-VLESS-WS-133MS` (url=254ms, nekobox=282ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-145MS` (url=247ms, nekobox=230ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-139MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-144MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-143MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-143MS` (url=271ms, nekobox=306ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS` (url=233ms, nekobox=225ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-145MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-147MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-136MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-151MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-146MS` (url=272ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-348MS` (url=712ms, status=HTTP 204)
15. `AKUN-015-CONFLU-VLESS-WS-357MS` (url=681ms, status=HTTP 204)
16. `AKUN-017-WPENG-VLESS-WS-378MS` (url=743ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-377MS` (url=796ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-394MS` (url=3204ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-395MS` (url=755ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-388MS` (url=753ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-224MS` (url=362ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-490MS` (url=948ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-631MS` (url=1024ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
