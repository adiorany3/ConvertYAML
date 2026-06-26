# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-101MS` (url=292ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-126MS` (url=261ms, nekobox=289ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-140MS` (url=291ms, nekobox=326ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-117MS` (url=308ms, nekobox=307ms, status=yes)
5. `AKUN-005-KIRINO-31-25-88-0-24-VLESS-WS-133MS` (url=268ms, nekobox=282ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-139MS` (url=301ms, nekobox=277ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-132MS` (url=283ms, nekobox=216ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-135MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-139MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-268MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-269MS` (url=3793ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-327MS` (url=605ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-300MS` (url=602ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-363MS` (url=728ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-383MS` (url=678ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-323MS` (url=669ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-302MS` (url=690ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-347MS` (url=708ms, status=HTTP 204)
20. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-563MS` (url=1008ms, status=HTTP 204)
21. `AKUN-033-CLOUDFLARE-VLESS-WS-694MS` (url=1020ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
