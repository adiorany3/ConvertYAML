# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 10
- Kandidat strict NekoBox-tested: 9
- Proxy di openclash_fresh_pool.yaml: 16

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=252ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, nekobox=241ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=222ms, nekobox=266ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-108MS` (url=237ms, nekobox=236ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-383MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-391MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-381MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-396MS`
9. `AKUN-023-UNKNOWN-VLESS-WS-709MS` (url=1024ms, nekobox=801ms, status=no)
10. `AKUN-009-KAWAII520-VLESS-WS-674MS`

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
