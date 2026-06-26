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
1. `AKUN-001-UNKNOWN-VLESS-WS-139MS` (url=285ms, nekobox=305ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS` (url=338ms, nekobox=322ms, status=yes)
3. `AKUN-003-1PASSWORD-VLESS-WS-156MS` (url=252ms, nekobox=311ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-154MS` (url=275ms, nekobox=322ms, status=yes)
5. `AKUN-005-ORACLE-VLESS-WS-162MS` (url=260ms, nekobox=293ms, status=yes)
6. `AKUN-006-UK-GB-DCL-01-20191003-VLESS-WS-155MS` (url=304ms, nekobox=325ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS` (url=273ms, nekobox=312ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-144MS` (url=254ms, nekobox=231ms, status=no)
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-144MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-169MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-152MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-154MS` (url=282ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-149MS` (url=268ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-165MS` (url=304ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-177MS` (url=276ms, status=HTTP 204)
16. `AKUN-016-CLOUDWEBMANAGE-EU-FR-VLESS-WS-151MS` (url=267ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-205MS` (url=263ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=277ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-305MS` (url=501ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-368MS` (url=711ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-372MS` (url=702ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-366MS` (url=723ms, status=HTTP 204)
23. `AKUN-024-OCTOPUSSS5-VLESS-WS-384MS` (url=794ms, status=HTTP 204)
24. `AKUN-025-SPEEDTEST-VLESS-WS-388MS` (url=797ms, status=HTTP 204)
25. `AKUN-026-WPENG-VLESS-WS-397MS` (url=783ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
