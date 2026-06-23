# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 16
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 22

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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=299ms, nekobox=333ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-139MS` (url=257ms, nekobox=329ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-133MS` (url=255ms, nekobox=299ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=291ms, nekobox=304ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-147MS` (url=307ms, nekobox=367ms, status=yes)
6. `AKUN-006-AMAZON-VLESS-WS-147MS` (url=307ms, nekobox=321ms, status=yes)
7. `AKUN-007-BROADNNET-KR-VLESS-WS-168MS` (url=337ms, nekobox=355ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-165MS` (url=259ms, nekobox=305ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-142MS` (url=282ms, nekobox=307ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-173MS` (url=260ms, nekobox=313ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-344MS` (url=773ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-379MS` (url=800ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-365MS` (url=650ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-410MS` (url=797ms, status=HTTP 204)
15. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-361MS` (url=756ms, status=HTTP 204)
16. `AKUN-021-UNKNOWN-VLESS-WS-568MS` (url=819ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
