# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-98MS` (url=241ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-125MS` (url=259ms, nekobox=333ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=222ms, nekobox=242ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-136MS` (url=234ms, nekobox=306ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS` (url=232ms, nekobox=259ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=282ms, nekobox=310ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-410MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-404MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-432MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-420MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-429MS` (url=883ms, status=HTTP 204)
12. `AKUN-013-BROADNNET-KR-VLESS-WS-169MS` (url=301ms, status=HTTP 204)
13. `AKUN-017-CLOUDFLARE-VLESS-WS-381MS` (url=763ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-381MS` (url=770ms, status=HTTP 204)
15. `AKUN-020-DEV-VLESS-WS-534MS` (url=722ms, status=HTTP 204)
16. `AKUN-027-CLOUDFLARE-VLESS-WS-778MS` (url=1034ms, status=HTTP 204)
17. `AKUN-030-CLOUDFLARE-VLESS-WS-730MS` (url=3965ms, status=HTTP 204)
18. `AKUN-034-RS-RAPIDSEEDBOX-20190717-VLESS-WS-844MS` (url=3370ms, status=HTTP 204)
19. `AKUN-035-CLOUDFLARE-VLESS-WS-892MS` (url=4639ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
